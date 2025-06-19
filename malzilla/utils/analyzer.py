import hashlib
import os

def get_file_info(file_path):
    """
    Returns file name, type (MIME, extension, description), and size in bytes.
    """
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    mime_type = None
    desc = None
    ext_type = os.path.splitext(file_name)[1].lower().lstrip('.')
    # Try python-magic
    try:
        import magic
        try:
            mime_type = magic.Magic(mime=True).from_file(file_path)
            desc = magic.Magic(mime=False).from_file(file_path)
        except Exception:
            pass
    except Exception:
        pass
    # Try filetype as fallback
    if not mime_type:
        try:
            import filetype
            kind = filetype.guess(file_path)
            if kind:
                mime_type = kind.mime
                desc = kind.extension
        except Exception:
            pass
    # Fallback to extension
    if not mime_type:
        mime_type = f"application/{ext_type}" if ext_type else "Unknown"
    if not desc:
        desc = ext_type if ext_type else "Unknown"
    return file_name, mime_type, file_size, desc

def yara_scan(file_path, rules_path="yara_rules.yar"):
    """
    Scan file with YARA rules if available.
    """
    try:
        import yara
        if os.path.exists(rules_path):
            rules = yara.compile(filepath=rules_path)
            matches = rules.match(file_path)
            return [m.rule for m in matches]
    except Exception:
        pass
    return []

def get_hashes(file_path):
    """
    Returns a dictionary of common hashes: MD5, SHA1, SHA256
    """
    hashes = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256(),
    }
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            for h in hashes.values():
                h.update(chunk)
    return {algo: h.hexdigest() for algo, h in hashes.items()}
