# Data Science Report

## 📌 Fine-tuning Setup
- **Target Task:** Summarization & domain-specific QA  
- **Dataset:** Mix of custom QA pairs + open-source summarization datasets (PubMed, arXiv abstracts)  
- **Method:** LoRA (Low-Rank Adaptation)  
- **Results:**  
  - Reduced hallucination rate by ~25%  
  - More concise & factual summaries  
  - Training efficiency improved vs full fine-tuning  

---

## 📏 Evaluation Methodology
1. **Automatic Metrics**  
   - BLEU, ROUGE for text similarity  
   - Precision/Recall for factual grounding  

2. **Human Evaluation**  
   - Accuracy of retrieved info  
   - Relevance to query  
   - Readability & coherence  

---

## 📊 Outcomes
- **Accuracy:** 82% (improved vs baseline GPT ~70%)  
- **ROUGE-L:** +12% improvement post fine-tuning  
- **Qualitative Feedback:** More structured, domain-appropriate answers  

---

## 💡 Observations
- Fine-tuning helped in making answers more “research-like”  
- Multi-agent delegation improved reliability  
- Limitation: Retrieval quality depends on source availability  
