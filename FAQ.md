# ❓ Frequently Asked Questions

Common questions about the 100 Days of AI Engineer program.

---

## 🎯 General Questions

### What is this program?

A structured 100-day curriculum to become a job-ready AI Engineer. It's project-focused, hands-on, and covers the modern AI stack from classical ML to LLMs and production deployment.

### Who is this for?

- Python developers wanting to transition to AI/ML
- Data analysts wanting to move into AI Engineering
- Computer science students
- Self-taught programmers
- Anyone with Python basics and determination

### What are the prerequisites?

**Required:**
- Python programming knowledge (functions, classes, loops, data structures)
- Basic command line usage
- Git basics (optional but recommended)

**Nice to have:**
- Math: Linear algebra, calculus, statistics (we'll review these)
- Previous ML exposure (not required)

### Do I need a powerful computer?

**Minimum:** 8GB RAM, multi-core CPU
**Recommended:** 16GB+ RAM, NVIDIA GPU

**Don't have a good machine?** Use free cloud resources:
- Google Colab (free GPU)
- Kaggle Notebooks (free GPU/TPU)
- AWS/GCP free tiers

### How much time per day?

**Recommended:** 6-8 hours daily

**Minimum to stay on track:** 1.5-2 hours

**Reality:** Some days will be 30 minutes, others 6 hours. Consistency matters more than daily perfection.

### Can I do this part-time?

**Absolutely!** Adjust the timeline:
- **2 hours/day:** Complete in ~100 days
- **1 hour/day:** Complete in ~200 days (still great!)
- **4 hours/day:** Complete in ~50 days

The "100 days" is a guideline, not a rule.

### Is this completely free?

**Yes, the curriculum is free!**

**Optional paid resources:**
- OpenAI API credits for GPT (~$20-50 for all projects)
- Cloud computing (AWS/GCP/Azure) - Free tiers available
- Courses (DeepLearning.AI, Coursera) - Many have free audit options
- Books - Most recommended books have free online versions

**You can complete everything with $0-50 total.**

---

## 📚 Learning & Progress

### What if I don't understand something?

**Normal!** AI/ML is complex. Try:

1. **Re-read slowly:** Complex concepts need multiple reads
2. **Use analogies:** Search "[concept] explained simply"
3. **Ask AI assistants:** ChatGPT/Claude are great tutors
4. **Watch videos:** Some people learn better visually
5. **Ask community:** Reddit, Discord, Stack Overflow
6. **Skip and return:** Sometimes later concepts clarify earlier ones

**Remember:** Everyone struggles. Persistence wins.

### Should I complete every single day in order?

**Recommended:** Yes, it's designed progressively.

**Reality:** Life happens. If you need to:
- Skip to a specific topic → Do it
- Spend extra days on hard topics → Do it
- Rearrange order → Do it

**Make it work for your situation.**

### What if I fall behind?

**Don't quit!** Options:

1. **Continue from where you left off**
2. **Adjust timeline:** Make it "200 Days"
3. **Focus on core:** Skip some mini-projects, focus on major ones
4. **Fast-forward:** If experienced, skip familiar topics

**Progress > Perfection**

### How do I know if I'm learning effectively?

**Good signs:**
- Can explain concepts simply
- Can implement from scratch (not just copy-paste)
- Projects work and you understand why
- Can debug errors independently
- Can modify code for new use cases

**Warning signs:**
- Just copying code without understanding
- Can't explain what you built
- Skip debugging ("I'll figure it out later")
- Not building projects

### Should I take notes?

**Yes!** But keep it practical:

- **Code comments:** Explain tricky parts
- **Jupyter notebooks:** Markdown cells for concepts
- **Daily logs:** Use provided template
- **Personal wiki:** Notion, Obsidian, etc.

**Don't:** Spend more time note-taking than coding.

### Can I build my own projects instead of suggested ones?

**Absolutely! That's even better!**

The suggested projects are templates. If you have a specific problem you want to solve or domain you're passionate about, go for it!

**Examples:**
- Hate the plant disease project? Build a face recognition system
- Love sports? Build a sports prediction model
- Into finance? Build a stock analyzer

**Just ensure it covers the same concepts.**

---

## 💻 Technical Questions

### Python or R?

**Python.** This curriculum uses Python because:
- Industry standard for AI/ML
- Better deep learning support
- Stronger ecosystem for production

R is great for statistics but Python dominates AI engineering.

### PyTorch or TensorFlow?

**We focus on PyTorch** because:
- More intuitive
- Preferred in research
- Growing in industry
- Easier to debug

TensorFlow is still valuable and concepts transfer easily.

### Do I need to know math deeply?

**It depends:**

**To use AI/ML tools:** Basic understanding is enough
**To build advanced models:** Deeper math helps
**To do research:** Yes, strong math foundation needed

**This program:** We cover essential math with intuition, not rigorous proofs. You'll learn enough to be productive.

**Can always go deeper later.**

### Can I use M1/M2 MacBook?

**Yes!** PyTorch has Apple Silicon support:

```bash
pip install torch torchvision torchaudio
```

Use MPS (Metal Performance Shaders) for acceleration:

```python
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
```

**Note:** Some packages might have compatibility issues. Use Colab as backup.

### What about Windows?

**Works great!** All tools support Windows.

**Tip:** Use WSL2 (Windows Subsystem for Linux) for better compatibility with some tools.

### Docker vs local installation?

**Start with local** for learning - easier to experiment.

**Use Docker** for:
- Deployment (Phase 6)
- Complex dependencies
- Reproducibility

You'll learn Docker in the MLOps phase.

---

## 🚀 Career & Applications

### Will this make me job-ready?

**Yes, but with caveats:**

**After 100 days you'll have:**
- Strong foundation in ML/DL
- Multiple projects in portfolio
- Hands-on experience with modern tools
- Understanding of production systems

**For entry-level roles:** Absolutely qualified

**For senior roles:** You'll need more experience

**Boost your chances:**
- Contribute to open source
- Write blog posts about learnings
- Network on LinkedIn/Twitter
- Apply early and often
- Do informational interviews

### What jobs can I get?

**Directly applicable:**
- Junior ML Engineer
- AI Engineer
- ML Ops Engineer (after Phase 6)
- Computer Vision Engineer
- NLP Engineer
- Data Scientist (with stats knowledge)

**Related transitions:**
- Software Engineer (AI-focused products)
- Research Engineer
- Applied Scientist

**Typical salary range (US, entry-level):** $80k-120k

### Do I need a degree?

**Not necessarily, but:**

**With degree (CS/Math/Engineering):** Easier to get interviews

**Without degree:** Need to prove yourself through:
- Strong portfolio projects
- Contributions to open source
- Technical blog posts
- Kaggle competitions
- Personal brand on social media

**Many companies** (especially startups) now hire based on skills, not degrees.

**This program helps** by giving you concrete projects to show.

### Should I do Kaggle competitions?

**Benefits:**
- Real-world problems
- Benchmark your skills
- Learn from top solutions
- Great for portfolio

**Downsides:**
- Can be time-consuming
- Overfitting to competition tricks
- Less focus on production/deployment

**Recommendation:** Do 2-3 competitions after Day 60 to test your skills.

### What's the difference between ML Engineer and Data Scientist?

**Simplified:**

**Data Scientist:**
- Exploratory analysis
- Statistical modeling
- Business insights
- Research-oriented
- Tools: Python, R, SQL, Tableau

**ML Engineer:**
- Building ML systems
- Production deployment
- Scalability & performance
- Engineering-oriented
- Tools: Python, PyTorch, Docker, Kubernetes

**This program** leans toward ML Engineering but covers both.

**Reality:** Titles vary by company. Job description matters more than title.

---

## 🤝 Community & Support

### Is there a community for this?

This is an open curriculum. You can:
- Create study groups
- Join r/learnmachinelearning
- Use #100DaysOfCode and #100DaysOfAIEngineer hashtags
- Join ML Discord servers
- Find accountability partners

### Can I share my progress publicly?

**Please do!** Benefits:
- Accountability
- Feedback from others
- Networking
- Helps others
- Portfolio for employers

**Share on:**
- Twitter/LinkedIn (daily updates)
- GitHub (code)
- Blog (detailed writeups)
- YouTube (if you like video)

### How can I contribute to this curriculum?

**Ways to contribute:**
- Fix typos or errors (open PR)
- Add resources
- Share your experience
- Create example projects
- Translate to other languages
- Suggest improvements

### Can I teach/share this with others?

**Absolutely!** This is open source.

**You can:**
- Share with friends
- Use in study groups
- Create YouTube series following it
- Write blog posts about it
- Teach classes using it

**Just:** Give credit and link back to original.

**Can't:** Sell it or claim as your own work.

---

## 🎯 Specific Topics

### Do we cover reinforcement learning?

**Briefly** in Phase 7 (advanced topics).

**Why not more?** RL is specialized and less common in industry roles. Better to master supervised/unsupervised learning first.

**If interested:** Dedicate extra time or do a separate 100-day RL journey after.

### What about MLOps/Production?

**Yes! Entire Phase 6 (Days 76-85)** covers:
- Model deployment
- Docker
- APIs (FastAPI)
- CI/CD
- Monitoring
- Cloud platforms

**This is crucial** and sets you apart from bootcamp graduates.

### Are LLMs covered enough?

**Yes! Phase 5 (Days 61-75)** covers:
- LLM fundamentals
- Fine-tuning
- Prompt engineering
- RAG systems
- LangChain
- Vector databases
- Production LLM apps

**Very current** and matches 2024-2025 job market demands.

### What about audio/speech?

**Lightly covered** in Phase 7 (Whisper model).

**If interested in speech ML:** Dedicate extra time to:
- Speech recognition (ASR)
- Text-to-Speech (TTS)
- Audio classification
- Librosa for audio processing

### Is SQL covered?

**Not directly.** This focuses on ML/AI engineering.

**But:** SQL is important for real work. Spend 1-2 days learning:
- Basic queries (SELECT, WHERE, JOIN)
- Aggregations (GROUP BY)
- Window functions

**Resources:** Mode Analytics SQL Tutorial, SQLBolt

---

## 🔧 Troubleshooting

### "Import Error: No module named X"

```bash
# Make sure environment is activated
conda activate ai-engineer

# Install the package
pip install X
```

### "CUDA out of memory"

```python
# Reduce batch size
batch_size = 16  # try 8, 4, or even 2

# Clear cache
torch.cuda.empty_cache()

# Use gradient checkpointing
model.gradient_checkpointing_enable()
```

### Code runs too slowly

**Options:**
1. Use GPU (Colab if you don't have one)
2. Reduce data size for experiments
3. Use smaller model
4. Optimize code (vectorization, caching)
5. Use cloud compute

### "My model accuracy is terrible"

**Debug checklist:**
- [ ] Data loaded correctly?
- [ ] Labels match predictions?
- [ ] Features scaled properly?
- [ ] Learning rate too high/low?
- [ ] Enough training epochs?
- [ ] Model capacity sufficient?
- [ ] Check for bugs in loss function

### Can't understand research papers

**Normal!** Try:
1. Read abstract + conclusion first
2. Look at figures and tables
3. Read introduction
4. Skip dense math on first read
5. Find blog posts explaining the paper
6. Watch paper review videos (Yannic Kilcher)
7. Re-read after implementing

**Papers get easier** with practice.

---

## 📅 After 100 Days

### What's next after completing?

**Options:**

1. **Get a job:** You're ready for entry-level positions

2. **Specialize:** Deep dive into CV, NLP, or MLOps

3. **Advanced topics:**
   - Reinforcement learning
   - Graph neural networks
   - Generative models (GANs, Diffusion)
   - Model optimization & quantization

4. **Research:** Start reading papers, replicating studies

5. **Build a startup:** Use your skills for your own product

6. **Open source:** Contribute to major libraries

7. **Content creation:** Blog, YouTube, courses

### How do I stay current?

**AI moves fast!** To stay updated:

**Daily (5-10 min):**
- Check Hugging Face papers
- Scan r/MachineLearning

**Weekly:**
- Read AI newsletters (The Batch, Import AI)
- Watch paper review videos

**Monthly:**
- Read 1-2 important papers fully
- Try new tools/frameworks
- Attend virtual meetups

**Don't:** Try to learn everything. Focus on depth in your area.

### Should I do a master's degree?

**Depends:**

**Get Master's if:**
- Want to do research
- Targeting top tech companies (helps but not required)
- Career change and need credentials
- Company will pay for it

**Skip if:**
- Already getting job offers
- Want to start working/earning
- Self-learning is working well
- High cost vs. benefit in your situation

**Compromise:** Work for 2-3 years, then do part-time Master's if needed.

---

## 💬 Mindset & Motivation

### I'm feeling overwhelmed

**Normal!** AI/ML is vast. Remember:

- You don't need to know everything
- Focus on one day at a time
- Take breaks when needed
- Review basics if lost
- Ask for help

**Imposter syndrome is real.** Everyone feels it, even experts.

### How do I stay motivated?

**Strategies:**

1. **Track progress:** Visual streak is motivating
2. **Share publicly:** Accountability + encouragement
3. **Join study group:** Others keep you going
4. **Remember your why:** Why did you start?
5. **Celebrate wins:** Built something cool? Celebrate!
6. **Mix it up:** Stuck? Work on different project
7. **Take days off:** Rest prevents burnout

### What if I want to quit?

**Before quitting:**

1. **Take a 2-3 day break** (not failure, necessary rest)
2. **Review progress:** How far you've come
3. **Adjust plan:** Make it easier if needed
4. **Change approach:** Different resources, projects
5. **Remember:** Slow progress > no progress

**Still want to quit?**

That's okay. Maybe:
- Wrong time in life
- Different interests discovered
- Need different approach

**You can always come back.** The curriculum will be here.

---

## 🎓 Success Stories

### Will update with community success stories as they come in!

**Share yours:**
- Completed the program?
- Got a job?
- Built something cool?

**Let us know!** We'll feature success stories to motivate others.

---

## ❓ Still Have Questions?

**Ask them:**
- Open an issue on GitHub
- Join the Discord community
- Email: [if applicable]
- Twitter: [if applicable]

**We'll update this FAQ** with commonly asked questions!

---

**Now stop reading and start coding!** 🚀

The only way out is through. Let's go! 💪
