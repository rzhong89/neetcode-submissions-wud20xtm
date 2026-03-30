class Solution {
    Set<Pair<Integer, Integer>> path = new HashSet<>();
    public boolean exist(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (backtrack(board, word, r, c, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

    public boolean backtrack(char[][] board, String word, int r, int c, int i) {
        if (i == word.length()) {
            return true;
        }

        if (r < 0 || c < 0 || r >= board.length || 
        c >= board[0].length || board[r][c] != word.charAt(i) || 
        path.contains(new Pair<>(r, c))) {
            return false;
        }

        path.add(new Pair<>(r, c));
        boolean res = backtrack(board, word, r + 1, c, i + 1) || 
        backtrack(board, word, r - 1, c, i + 1) || 
        backtrack(board, word, r, c + 1, i + 1) ||
        backtrack(board, word, r, c - 1, i + 1);
        path.remove(new Pair<>(r, c));
        return res;
    }
}
