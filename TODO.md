## What Needs to Be Refactored?

### Code Quality

- [x] Avoid repeating magic numbers
- [x] Use more descriptive variable and function names
- [x] Make boolean function names more expressive (`is_`, `has_`, `can_`)
- [x] Replace nested conditionals with early returns where appropriate
- [x] Move repeated behavior into reusable functions
- [x] Move repeated data into constants

### Architecture

- [ ] Reduce duplicate logic between DFS and BFS
- [ ] Separate pattern validation from search algorithms
- [ ] Consider extracting pattern rules into a dedicated class

### Performance

- [ ] Benchmark DFS vs BFS performance
- [ ] Investigate memory usage of BFS
- [ ] Replace list queue with a more efficient queue implementation

### Testing

- [ ] Verify total number of generated patterns
- [ ] Test all middle-dot validation rules
- [ ] Add edge-case tests

### Documentation

- [ ] Add algorithm complexity analysis
- [ ] Add diagrams explaining DFS and BFS traversal
- [ ] Document the validation process in more detail