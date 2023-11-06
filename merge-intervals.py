# take a list of intervals as input, each interval represented as an object with attributes start and end.
# initialize an empty list called out to store the merged intervals.
# use the sorted(), sort the input intervals in ascending order based on their start attribute, lambda function as the key.

def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
