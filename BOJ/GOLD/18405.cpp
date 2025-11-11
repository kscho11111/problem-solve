#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <utility>

using std::cout;
using std::cin;
using std::queue;
using std::pair;
using std::make_pair;
using std::endl;

int N, K, S, X, Y, arr[200][200], temp[200][200];
queue<pair<int,int>> q, nq;

int nRow[4] = {0, 0, 1, -1};
int nCol[4] = {1, -1, 0, 0};

bool isOut(int row, int col){
    return (row < 0 || row >= N || col < 0 || col >= N);
}

void reset();
void input();
void virus();
void print();

int main(){
    reset();
    input();
    virus();
    print();
}

void reset(){
    memset(arr, 0, sizeof(arr));
    memset(temp, 0, sizeof(temp));
}

void input(){
    cin >> N >> K;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> arr[i][j];
            if(arr[i][j]){
                q.push(make_pair(i,j));
            }
        }
    }

    cin >> S >> X >> Y;
}

void virus(){
    while(S--){
        int size = q.size();
        for(int i = 0; i < size; i++){
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            for(int j = 0; j < 4; j++){
                int nextrow = row + nRow[j];
                int nextcol = col + nCol[j];

                if(!isOut(nextrow, nextcol) && arr[nextrow][nextcol] == 0){
                    if(!temp[nextrow][nextcol]){
                        temp[nextrow][nextcol] = arr[row][col];
                        nq.push(make_pair(nextrow,nextcol));
                    }
                    else if(temp[nextrow][nextcol] > arr[row][col])
                        temp[nextrow][nextcol] = arr[row][col];
                }
            }
        }

        q = nq;
        while(!nq.empty()){
            int row = nq.front().first;
            int col = nq.front().second;
            arr[row][col] = temp[row][col];
            nq.pop();
        }
    }
}

void print(){
    cout << arr[X-1][Y-1] << endl;
}