#include <bits/stdc++.h>

using namespace std;

int N, num, k, arr[2187][2187];
bool visited[2187][2187];

void reset();
void input();
void star();
void print();

int main()
{
    reset();
    input();
    star();
    print();
}

void reset(){
    memset(arr, 0, sizeof(arr));
    memset(visited, false, sizeof(visited));
}

void input(){
    cin >> N;
    num = N;
    k = 0;

    while(num > 1){
        num /=3;
        k++;
    }
    //cout << k << "\n";
}

void star(){
    while(k > 0){
        int p = 1;
        for(int i = 0; i < k-1; i++){
            p *= 3;
        }
        //cout << p << "\n";
        int r = 3*p;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(i / p == 1 && j / p ==1){
                    visited[i][j] = true;
                    for(int a = i; a < N; a+=r){
                        for(int b = j; b < N; b+=r){
                            visited[a][b] = true;
                            //cout << a << " " << b << "\n";
                        }
                    }
                }
            }
        }
        k--;
    }
}

void print(){
    for(int i = 0; i < N; i++){
        for(int j =0; j < N; j++){
            if(!visited[i][j]){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << "\n";
    }
}