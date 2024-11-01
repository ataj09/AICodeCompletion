# Code Completion Evaluation Report

## 1. Introduction
The objective of this experiment was to evaluate the performance of a code completion model using a custom dataset. The model was assessed based on its ability to predict missing code snippets in Python functions from a pre-existing codebase.

## 2. Dataset Creation
The dataset was created by:
1. Selecting files from a custom repository.
2. Dividing each file into three segments: 
   - **Prefix**: Code before the cursor (provided as context).
   - **Middle**: The missing code (used as the ground truth).
   - **Suffix**: Code following the cursor (providing further context).

Each example included a **prefix**, **middle_actual** (ground truth), **middle_predicted** (model's prediction), and a **suffix**. This resulted in a dataset with examples labeled as "correct" or "incorrect," depending on the logical consistency and correctness of `middle_predicted` compared to `middle_actual`.

## 3. Evaluation Metrics
The model's performance was evaluated using the following automatic metrics:

- **Average BLEU Score**: 0.0242
- **Exact Match**: 0.0000
- **Average Levenshtein Distance**: 866.5000
- **Average CHRF Score**: 22.0180

## 4. Metrics Explanation
- **BLEU Score**: Measures n-gram overlap between `middle_predicted` and `middle_actual`. BLEU values closer to 1 indicate high similarity, but the low score here (0.0242) suggests minimal overlap between predictions and ground truth.
- **Exact Match**: Indicates if the predicted code exactly matches the actual code. In this case, an Exact Match of 0.0000 indicates no exact matches, reflecting the model’s difficulty in reproducing the precise logic of the original code.
- **Levenshtein Distance**: Quantifies the number of single-character edits required to change the predicted code to the actual code. An average of 866.5 suggests significant differences between predictions and ground truth.
- **CHRF Score**: An n-gram-based metric that evaluates character-level similarity, particularly suitable for shorter, language-specific strings like code. The CHRF score of 22.0180 reflects limited similarity.

## 5. Findings
- **Correctness**: The model struggled to generate correct code predictions that aligned closely with the actual logic in `middle_actual`, as reflected in low BLEU and CHRF scores and a high Levenshtein distance.
- **Exact Matching Issues**: With zero exact matches, the model consistently failed to replicate exact sequences, likely due to the context-sensitive nature of code and the unique logic within functions.
- **Logic Consistency**: The manual labeling process highlighted the challenges of predicting not just syntactically correct but logically coherent code. For example, when completing function definitions or implementing calculations, the model’s outputs often diverged from expected outcomes.
- **Length to correctness**: Manual labeling provided insight of correctness being heavly influenced by similarity of length of both predicted 
and actual code.

## 6. Learnings and Future Work
The experiment demonstrates the limitations of using general-purpose code models in tasks requiring high logical consistency and correctness. Improvements may include:
1. **Data Augmentation**: Providing additional context or more examples per function type could improve prediction accuracy,
2. **Domain-Specific Fine-Tuning**: Fine-tuning on similar codebases with aligned logic requirements might improve results.
Using individual developer writing style could improve the model output.
3. **Advanced Metrics**: Employing CodeBLEU and functional correctness metrics, which factor in logical outcomes, could yield more insightful assessments.
---

## 7. Conclusion
This evaluation revealed that while the code completion model could produce code syntactically, it struggled with generating correct, logically consistent snippets, as evidenced by low BLEU, CHRF, and exact match scores. Future steps could focus on model adjustments and dataset enhancements to improve logical coherence in code predictions.
