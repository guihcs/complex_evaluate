# Complex Evaluate

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
![PyPI - Version](https://img.shields.io/pypi/v/complex-evaluate)
[![Tests](https://github.com/guihcs/complex_evaluate/actions/workflows/tests.yml/badge.svg)](https://github.com/guihcs/complex_evaluate/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/guihcs/complex_evaluate/graph/badge.svg?token=2CJVVVJQXB)](https://codecov.io/github/guihcs/complex_evaluate)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Python library for evaluating complex ontology alignments in [EDOAL](https://moex.gitlabpages.inria.fr/alignapi/edoal.html) (Expressive and Declarative Ontology Alignment Language) format adapting precision, recall, and f-measure metrics to the complex matching case.

## Highlights

- Evaluate EDOAL alignments from files or in-memory strings.
- Weighted precision/recall for simple vs. complex mappings.
- Built on an unordered tree edit distance similarity measure.

## Quickstart

Install the library:
```bash
pip install complex-evaluate
```

Evaluate alignments from EDOAL files:

```python
from complex_evaluate.evaluate import evaluate_edoal

precision, recall, f_measure = evaluate_edoal(
    "predicted_alignment.edoal",
    "reference_alignment.edoal",
)

print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F-measure: {f_measure:.3f}")
```

Or evaluate directly from EDOAL strings:

```python
from complex_evaluate.evaluate import evaluate_edoal_string

predicted = '''<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
         xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#">
  <Alignment>
    <map>
      <Cell>
        <entity1>
          <Class rdf:about="http://example.org#ClassA" />
        </entity1>
        <entity2>
          <Class rdf:about="http://example.org#ClassB" />
        </entity2>
      </Cell>
    </map>
  </Alignment>
</rdf:RDF>'''

reference = predicted  # Use same for identity test

p, r, f = evaluate_edoal_string(predicted, reference)
print(f"F-measure: {f}")  # Should be 1.0 for identical alignments
```

## What next

- Read the [installation guide](installation.md).
- See usage patterns in the [usage guide](usage.md).
- Browse the [API reference](api.md).
