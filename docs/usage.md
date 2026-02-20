# Usage

## Evaluate alignments from files

```python
from complex_evaluate.evaluate import evaluate_edoal

precision, recall, f_measure = evaluate_edoal(
    "predicted_alignment.edoal",
    "reference_alignment.edoal",
)

print(precision, recall, f_measure)
```

## Evaluate alignments from strings

```python
from complex_evaluate.evaluate import evaluate_edoal_string

predicted = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"
         xmlns=\"http://knowledgeweb.semanticweb.org/heterogeneity/alignment#\">
  <Alignment>
    <map>
      <Cell>
        <entity1>
          <Class rdf:about=\"http://example.org#ClassA\" />
        </entity1>
        <entity2>
          <Class rdf:about=\"http://example.org#ClassB\" />
        </entity2>
      </Cell>
    </map>
  </Alignment>
</rdf:RDF>"""

reference = predicted
p, r, f = evaluate_edoal_string(predicted, reference)
print(f"F-measure: {f}")
```

## Parameters

The main evaluation functions accept the following parameters:

- `w` (float): weight in `[0, 1]` for complex mappings. A higher value gives more weight to complex mappings in precision/recall aggregation.
- `sim_func` (callable): similarity function used to compare mapping trees. Defaults to `complex_evaluate.uted.u_sim`.
- `ignore_errors` (bool): when `True`, skips malformed mappings instead of raising.
