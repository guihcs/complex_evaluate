# API reference

## Evaluation

### `evaluate_edoal`

```python
evaluate_edoal(p1, p2, w=0.5, sim_func=u_sim, ignore_errors=False, soft=False)
```

- `p1`, `p2`: paths (or file-like objects) to EDOAL alignment documents.
- `w`: weight for complex mappings in precision/recall aggregation.
- `sim_func`: similarity function for mapping trees.
- `ignore_errors`: skip malformed mappings when `True`.
- `soft`: currently unused, reserved for future extensions.

Returns `(precision, recall, f_measure)`.

### `evaluate_edoal_string`

```python
evaluate_edoal_string(p1, p2, w=0.5, sim_func=u_sim, ignore_errors=False, soft=False)
```

- `p1`, `p2`: EDOAL XML strings.
- Other parameters and return values match `evaluate_edoal`.

## Unordered tree utilities

### `u_sim`

```python
u_sim(t1, t2, cache=None)
```

Computes unordered tree similarity in `[0, 1]`.

### `u_ted`

```python
u_ted(t1, t2, cache=None)
```

Computes unordered tree edit distance; returns `(distance, mapping)`.

### `tree_size`

```python
tree_size(t)
```

Returns the number of nodes in a tree.


