# Use sliding window when:
# Array or string
# Continous
# Asking for max / min, sum / count, longest /shortest

# Window = range [left > right]
# Right pointer moves forward
# Left pointer moves forward only when needed
# Never goes backwards
# Update results while sliding

# It is fast because it enters the window once, leaves the window once:
# O(n)

# Fixed sliding window
# Window size = k
# Example: max sum of size k

# Variable size window
# Based on a condition
# Example: longest substring without repeats