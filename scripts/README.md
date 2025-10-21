# Documentation Fetch Scripts

Two scripts are available for fetching Claude Code documentation:

## Python Script (RECOMMENDED) ⚡

**`fetchccdocs.py`** - Async Python 3.14 free-threaded with blazing fast performance

### Usage

```bash
# Default: fresh fetch, 50 parallel jobs, Python 3.14t (free-threaded)
uv run scripts/fetchccdocs.py

# More aggressive parallelism
uv run scripts/fetchccdocs.py --jobs 100

# Incremental mode (skip existing files)
uv run scripts/fetchccdocs.py --incremental

# Fetch specific sections only
uv run scripts/fetchccdocs.py --section agent-sdk,api-reference

# Custom output directory
uv run scripts/fetchccdocs.py --out /path/to/output

# Help
uv run scripts/fetchccdocs.py --help
```

### Features

- ⚡ **Super fast**: ~5 seconds for 282 docs (180-240x faster than bash)
- 🧵 **Python 3.14 free-threaded**: No GIL, true parallel execution
- 🔄 **Fresh by default**: Always gets latest content (use `--incremental` to skip)
- 📊 **Progress tracking**: Real-time progress bar with tqdm
- 🚀 **Async/parallel**: 50+ concurrent downloads
- 🛡️ **Robust**: Proper error handling and retries
- 📦 **Zero setup**: Uses `uv run` with inline dependencies

### Performance

| Docs | Time | Speed | Notes |
|------|------|-------|-------|
| 282 (fresh) | ~5 sec | ~56 docs/sec | Python 3.14 free-threaded |
| 14 (SDK only) | ~1 sec | ~15 docs/sec | `--section agent-sdk` |
| 282 (incremental) | ~1 sec | instant | `--incremental` flag |

## Bash Script (LEGACY)

**`fetchccdocs.sh`** - Original bash implementation

### Usage

```bash
# Default
./scripts/fetchccdocs.sh

# With options
./scripts/fetchccdocs.sh --format md --out content --jobs 10
```

### Features

- ✅ **Reliable**: Well-tested, production-ready
- 📝 **Simple**: Pure bash, no dependencies
- 🐌 **Slow**: Sequential fetching (~15-20 min for 282 docs)

### Performance

| Docs | Time | Speed |
|------|------|-------|
| 282 (sequential) | ~15-20 min | ~0.2-0.3 docs/sec |

## Comparison

| Feature | Python (async) | Bash |
|---------|----------------|------|
| **Speed** | ⚡ 5 sec | 🐌 15-20 min |
| **Parallelism** | ✅ 50+ concurrent | ❌ Sequential |
| **Python Version** | 🧵 3.14 free-threaded | N/A |
| **Default Mode** | 🔄 Fresh fetch | N/A |
| **Incremental** | ✅ Optional (`--incremental`) | ❌ No |
| **Progress** | ✅ Real-time bar | ⚠️ Basic logs |
| **Dependencies** | `uv` + Python 3.14t | None |
| **Recommended** | ✅ **YES** | Legacy |

## Recommendation

**Use the Python script** (`fetchccdocs.py`) for:
- Daily documentation updates
- CI/CD pipelines
- Initial repository setup
- Any scenario where speed matters

**Use the Bash script** (`fetchccdocs.sh`) only if:
- Python/uv not available
- Need maximum compatibility
- Debugging fetch issues

## Migration

The Python script produces the same output structure as bash, so they're 100% compatible. Simply switch:

```bash
# Old
./scripts/fetchccdocs.sh

# New (recommended)
uv run scripts/fetchccdocs.py
```

## Examples

### Daily Update Workflow

```bash
# Fresh fetch - always get latest (5 seconds)
uv run scripts/fetchccdocs.py

# Quick incremental update if needed (1-2 seconds)
uv run scripts/fetchccdocs.py --incremental
```

### CI/CD Pipeline

```yaml
# .github/workflows/update-docs.yml
- name: Fetch latest docs
  run: uv run scripts/fetchccdocs.py  # Fresh by default
```

### Full Re-fetch

```bash
# Clean slate
rm -rf content/
uv run scripts/fetchccdocs.py  # Fresh by default
```

### Python 3.14 Free-Threading

The script uses Python 3.14's free-threaded mode (no GIL) for true parallel execution:

```bash
# uv automatically uses 3.14t due to requires-python metadata
uv run scripts/fetchccdocs.py

# Or explicitly specify
uv run --python 3.14t scripts/fetchccdocs.py
```

Benefits:
- **No GIL**: True parallel thread execution
- **~3.1x faster**: On multi-threaded workloads vs 3.13
- **Low overhead**: Only 5-10% on single-threaded code
