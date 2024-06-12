#include <stdio.h>
#include <stdbool.h>

#define SIZE 3

void printBoard(char board[SIZE][SIZE]);
bool checkWin(char board[SIZE][SIZE], char player);
bool checkDraw(char board[SIZE][SIZE]);
void makeMove(char board[SIZE][SIZE], char player);

int main() {
    char board[SIZE][SIZE] = {
        {'1', '2', '3'},
        {'4', '5', '6'},
        {'7', '8', '9'}
    };

    char currentPlayer = 'X';
    bool gameEnded = false;

    while (!gameEnded) {
        printBoard(board);
        makeMove(board, currentPlayer);

        if (checkWin(board, currentPlayer)) {
            printBoard(board);
            printf("Player %c wins!\n", currentPlayer);
            gameEnded = true;
        } else if (checkDraw(board)) {
            printBoard(board);
            printf("The game is a draw!\n");
            gameEnded = true;
        } else {
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
    }

    return 0;
}

void printBoard(char board[SIZE][SIZE]) {
    printf("\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf(" %c ", board[i][j]);
            if (j < SIZE - 1) printf("|");
        }
        printf("\n");
        if (i < SIZE - 1) printf("---+---+---\n");
    }
    printf("\n");
}

bool checkWin(char board[SIZE][SIZE], char player) {
    for (int i = 0; i < SIZE; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true;
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true;
    }

    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;

    return false;
}

bool checkDraw(char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] != 'X' && board[i][j] != 'O') return false;
        }
    }
    return true;
}

void makeMove(char board[SIZE][SIZE], char player) {
    int move;
    bool validMove = false;

    while (!validMove) {
        printf("Player %c, enter your move (1-9): ", player);
        scanf("%d", &move);

        if (move >= 1 && move <= 9) {
            int row = (move - 1) / SIZE;
            int col = (move - 1) % SIZE;

            if (board[row][col] != 'X' && board[row][col] != 'O') {
                board[row][col] = player;
                validMove = true;
            } else {
                printf("The cell is already occupied. Try again.\n");
            }
        } else {
            printf("Invalid move. Enter a number between 1 and 9.\n");
        }
    }
}
