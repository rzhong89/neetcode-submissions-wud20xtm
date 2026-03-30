class MedianFinder {
    PriorityQueue<Integer> lowerHalf;
    PriorityQueue<Integer> upperHalf;

    public MedianFinder() {
        lowerHalf = new PriorityQueue<>(Comparator.reverseOrder());
        upperHalf = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        lowerHalf.add(num);
        if (lowerHalf.size() - upperHalf.size() > 1 || !upperHalf.isEmpty() && lowerHalf.peek() > upperHalf.peek()) {
            upperHalf.add(lowerHalf.poll());
        }
        if (upperHalf.size() - lowerHalf.size() > 1) {
            lowerHalf.add(upperHalf.poll());
        }
    }
    
    public double findMedian() {
        if (lowerHalf.size() == upperHalf.size()) {
            return (double) (lowerHalf.peek() + upperHalf.peek()) / 2; 
        } else if (lowerHalf.size() > upperHalf.size()) {
            return (double) lowerHalf.peek();
        } else {
            return (double) upperHalf.peek();
        }
    }
}
