# Complex Evaluate

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
![PyPI - Version](https://img.shields.io/pypi/v/complex-evaluate)
[![Tests](https://github.com/guihcs/complex_evaluate/actions/workflows/tests.yml/badge.svg)](https://github.com/guihcs/complex_evaluate/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/guihcs/complex_evaluate/graph/badge.svg?token=2CJVVVJQXB)](https://codecov.io/github/guihcs/complex_evaluate)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


A Python library for evaluating complex ontology alignments in [EDOAL](https://moex.gitlabpages.inria.fr/alignapi/edoal.html) (Expressive and Declarative Ontology Alignment Language) format adapting precision, recall, and f-measure metrics to the complex matching case.

### Requirements

- Python >= 3.9
- NumPy
- SciPy

## 📦 Installation

```bash
pip install complex-evaluate
```
## 📖 Usage

### Basic Example

```python
from complex_evaluate.evaluate import evaluate_edoal

# Compare two alignment files
precision, recall, f_measure = evaluate_edoal(
    'predicted_alignment.edoal',
    'reference_alignment.edoal'
)

print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F-measure: {f_measure:.3f}")
```

### Comparing from strings

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

## 📊 Use Cases

This metric was used in the evaluation of OAEI 2025 in the Complex Matching track https://oaei.ontologymatching.org/2025/results/complex/index.html.

Also, this library is particularly useful for:

- **Ontology Alignment Evaluation**: Benchmarking alignment approaches on complex matching tasks.
- **LLM reasoning training**: The metric can enable the training of LLMs to reason about complex alignments by providing a verifiable reward signal based on the score of the predicted alignment against a reference alignment.

## 🤝 Contributing

Contributions are welcome! Some areas for improvement:
- Additional similarity metrics.
- Performance optimizations.
- Support for other alignment formats.
- Extended documentation and examples.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Citation

If you use this library in your research, please cite it as follows:

```bibtex
@inproceedings{DBLP:conf/esws/SousaLS25,
  author       = {Guilherme Henrique Santos Sousa and
                  Rinaldo Lima and
                  C{\'{a}}ssia Trojahn dos Santos},
  title        = {On Evaluation Metrics for Complex Matching Based on Reference Alignments},
  booktitle    = {{ESWC} {(1)}},
  series       = {Lecture Notes in Computer Science},
  volume       = {15718},
  pages        = {77--93},
  publisher    = {Springer},
  year         = {2025}
}
```

---

*Built with ❤️ for the Semantic Web and Ontology Matching community.*

