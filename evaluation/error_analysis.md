# Evaluation Error Analysis

## Summary

The evaluation set contains 30 questions.

- Total questions: 30
- Faithful: 29
- Unfaithful: 1
- Faithfulness: 96.67%

## Failure Case

### Question

How can I improve account security?

### Expected Source

authentication.md

### Result

The retrieval evaluation successfully found the expected source, but the faithfulness approximation classified this case as unfaithful.

### Possible Cause

The question is broad and does not contain many specific keywords that directly overlap with the retrieved authentication document. Because the current faithfulness evaluation uses a simple keyword-overlap heuristic, a semantically relevant retrieval can still be classified as unfaithful.

### Analysis

This result does not necessarily mean that the RAG retrieval failed. The retrieval evaluation recorded this question as a successful retrieval case with Recall@3. The mismatch is related to the limitation of the current keyword-overlap faithfulness approximation.

### Improvement Plan

Future versions can improve this evaluation by using:

1. LLM-based faithfulness evaluation
2. Semantic similarity instead of simple keyword overlap
3. Query expansion for broad security questions
4. Improved chunking and retrieval settings

## Conclusion

The evaluation achieved 29 faithful cases out of 30. The single failure was analyzed as a limitation of the current heuristic evaluation method rather than a confirmed RAG retrieval failure.
