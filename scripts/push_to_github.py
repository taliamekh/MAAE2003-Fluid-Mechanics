#!/usr/bin/env python3
"""Push files to GitHub via the API. Usage:
  python3 push_to_github.py <file1> [file2 ...] --repo OWNER/REPO --token TOKEN --message "commit msg"
  OR pass all files in a directory:
  python3 push_to_github.py --dir . --repo OWNER/REPO --token TOKEN --message "commit msg"
"""
import argparse, base64, json, os, sys, urllib.request, urllib.error

API = "https://api.github.com"

def gh(method, path, token, data=None):
    url = f"{API}{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    if body:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode()) if r.status != 204 else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"  ✗ {method} {path} → {e.code}: {err[:200]}", file=sys.stderr)
        return None

def get_default_branch(repo, token):
    info = gh("GET", f"/repos/{repo}", token)
    return info["default_branch"] if info else "main"

def push_files(files, repo, token, message, branch=None):
    if not branch:
        branch = get_default_branch(repo, token)
    ref = gh("GET", f"/repos/{repo}/git/ref/heads/{branch}", token)
    if not ref:
        print(f"Branch '{branch}' not found — creating initial commit...", file=sys.stderr)
        blobs = []
        for fpath, repo_path in files:
            with open(fpath, "rb") as f:
                content = base64.b64encode(f.read()).decode()
            blob = gh("POST", f"/repos/{repo}/git/blobs", token,
                       {"content": content, "encoding": "base64"})
            if blob:
                blobs.append({"path": repo_path, "mode": "100644",
                              "type": "blob", "sha": blob["sha"]})
                print(f"  ✓ blob {repo_path}")
        tree = gh("POST", f"/repos/{repo}/git/trees", token, {"tree": blobs})
        if not tree:
            return False
        commit = gh("POST", f"/repos/{repo}/git/commits", token,
                     {"message": message, "tree": tree["sha"]})
        if not commit:
            return False
        result = gh("POST", f"/repos/{repo}/git/refs", token,
                     {"ref": f"refs/heads/{branch}", "sha": commit["sha"]})
        print(f"  ✓ Created branch '{branch}' with {len(blobs)} files")
        return bool(result)
    else:
        parent_sha = ref["object"]["sha"]
        blobs = []
        for fpath, repo_path in files:
            with open(fpath, "rb") as f:
                content = base64.b64encode(f.read()).decode()
            blob = gh("POST", f"/repos/{repo}/git/blobs", token,
                       {"content": content, "encoding": "base64"})
            if blob:
                blobs.append({"path": repo_path, "mode": "100644",
                              "type": "blob", "sha": blob["sha"]})
                print(f"  ✓ blob {repo_path}")
        tree = gh("POST", f"/repos/{repo}/git/trees", token,
                   {"base_tree": ref["object"]["sha"], "tree": blobs})
        if not tree:
            return False
        commit = gh("POST", f"/repos/{repo}/git/commits", token,
                     {"message": message, "tree": tree["sha"],
                      "parents": [parent_sha]})
        if not commit:
            return False
        result = gh("PATCH", f"/repos/{repo}/git/refs/heads/{branch}", token,
                     {"sha": commit["sha"]})
        print(f"  ✓ Pushed {len(blobs)} files to '{branch}'")
        return bool(result)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="*", help="Files to push (filepath:repopath or just filepath)")
    p.add_argument("--dir", help="Push all files in directory (recursive)")
    p.add_argument("--repo", required=True)
    p.add_argument("--token", required=True)
    p.add_argument("--message", default="Update notes")
    p.add_argument("--branch", default=None)
    args = p.parse_args()

    file_pairs = []
    if args.dir:
        base = os.path.abspath(args.dir)
        for root, dirs, fnames in os.walk(base):
            dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'node_modules')]
            for fn in fnames:
                if fn.startswith('.'):
                    continue
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, base)
                file_pairs.append((full, rel))
    else:
        for f in args.files:
            if ":" in f and not f.startswith("/"):
                fpath, rpath = f.split(":", 1)
            else:
                fpath = f
                rpath = os.path.basename(f)
            file_pairs.append((fpath, rpath))

    if not file_pairs:
        print("No files to push.", file=sys.stderr)
        sys.exit(1)

    ok = push_files(file_pairs, args.repo, args.token, args.message, args.branch)
    sys.exit(0 if ok else 1)
