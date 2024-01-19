#include <bits/stdc++.h>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main(){
    string str;

    while(true){
        int cnt = 0;
        getline(cin,str);
        if(str[0] == '#')
            break;
        else{
            for(int i = 0; i < str.length(); i++){
                if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')
                    cnt++;
            }
            cout << cnt << endl;
        }
    }


}