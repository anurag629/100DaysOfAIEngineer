# Scripts Directory

This directory contains utility scripts used for maintaining and generating the 100 Days of AI Engineer curriculum.

## 📜 Scripts Overview

### `generate_all_days.py`
**Purpose:** Bulk generator for all 100 daily checklist READMEs

**Usage:**
```bash
python scripts/generate_all_days.py
```

**What it does:**
- Generates comprehensive README.md files for all 100 days
- Assigns topics based on the DAY_TOPICS mapping
- Includes phase-appropriate tools and resources
- Creates both regular learning days and project days

**When to use:**
- After updating the daily template structure
- When making bulk changes to all days
- When regenerating content with new resources

---

### `resource_links.py`
**Purpose:** Centralized database of 350+ verified resource links (2024-2025)

**Contents:**
- Topic-specific learning resources
- Practice platforms (DataWars, Kaggle, etc.)
- Official documentation links
- Video tutorials and courses
- Interactive learning platforms

**Topics Covered:**
- NumPy & Pandas
- Data Visualization
- Machine Learning (scikit-learn)
- PyTorch & Deep Learning
- Computer Vision (YOLO, CNNs, Transformers)
- NLP & Transformers (BERT, GPT)
- LLMs & RAG Systems (LangChain)
- MLOps (MLflow, FastAPI, Docker)
- Advanced AI (Multi-modal, RL, Stable Diffusion)

**Usage:**
```python
from resource_links import get_resources_for_day

# Get resources for a specific day
resources = get_resources_for_day(1)  # Returns NumPy resources
resources = get_resources_for_day(71)  # Returns RAG resources
```

---

### `enhance_daily_checklists.py`
**Purpose:** Template generation engine for daily README files

**What it does:**
- Takes day data (objectives, resources, projects, etc.)
- Generates formatted README.md with consistent structure
- Includes all standard sections (prerequisites, time breakdown, resources, etc.)
- Adds CODERCOPS Discord integration

**Usage:**
```python
from enhance_daily_checklists import generate_enhanced_readme

data = {
    "topic": "NumPy Basics",
    "phase": "Phase 1: Foundations",
    "learning_objectives": [...],
    "resources": {...},
    # ... etc
}

content = generate_enhanced_readme(day_num=1, data=data)
```

---

## 🚀 Typical Workflow

**To regenerate all 100 days:**
```bash
cd /home/user/100DaysOfAIEngineer
python scripts/generate_all_days.py
```

**To update resource links:**
1. Edit `scripts/resource_links.py`
2. Add new links to appropriate topic categories
3. Run `generate_all_days.py` to apply changes

**To modify daily template structure:**
1. Edit `scripts/enhance_daily_checklists.py`
2. Update the `generate_enhanced_readme()` function
3. Run `generate_all_days.py` to regenerate all days

---

## 📝 Notes

- All scripts use absolute paths for reliability
- Resource links are verified and current (2024-2025)
- Scripts are designed to be idempotent (safe to run multiple times)
- All generated READMEs follow the same consistent structure

---

**For learners:** You don't need these scripts! They're only for curriculum maintenance.

**For contributors:** See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines (if available).
