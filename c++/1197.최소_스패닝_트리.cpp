#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int Find(vector<int>&parents, int now){
    if(parents[now] == now) return now;
    return parents[now] = Find(parents, parents[now]);
}

void Union(vector<int>&parents, int e1, int e2){
    if(Find(parents, e1) == Find(parents, e2)) return;
    parents[Find(parents, e2)] = Find(parents, e1);
}

bool IsUnion(vector<int>&parents, int e1, int e2){
    if(Find(parents, e1) == Find(parents, e2)) return true;
    return false;
}

void InsertionSort(vector<tuple<int,int,int>>& arr, int low, int high){
    for(int i = low + 1; i < high + 1; i++){
        tuple<int,int,int> now = arr[i];
        int nowI = i - 1;
        for(; nowI >= 0 && arr[nowI] > now; nowI--){
            arr[nowI + 1] = arr[nowI];
        }
        arr[nowI + 1] = now;
    }
}

int partition(vector<tuple<int,int,int>>& arr, int low, int high){
    int pivot = low;
    int left = low;
    int right = high + 1;
    do{
        do left++; while (arr[left] < arr[pivot] && left <= high);
        do right--; while (arr[right] > arr[pivot] && right >= low);
        if (left < right) swap(arr[left], arr[right]);
    } while(left < right);
    swap(arr[low], arr[right]);
    return right;
}

void QuickSort(vector<tuple<int,int,int>>& arr, int low, int high){
    if(low < high){
        if(high - low + 1 <= 6){
            InsertionSort(arr, low, high);
        }else{
            int pivot = partition(arr, low, high);
            QuickSort(arr, low, pivot - 1);
            QuickSort(arr, pivot + 1, high);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m;
    cin>>n>>m;
    vector<tuple<int, int, int>> edges;
    for(int i = 0; i < m; i++){
        int from, to, weight;
        cin >> from >> to >> weight;
        edges.push_back(tuple<int,int,int>(weight,from - 1,to - 1));
    }

    sort(edges.begin(), edges.end());
    for(int i = 0; i < edges.size(); i++){
        cout << i << ": " << get<0>(edges[i]) << ", " << get<1>(edges[i]) << ", " << get<2>(edges[i]) <<"\n";
    }
    vector<int> parents(n);
    for(int i = 0; i < parents.size(); i++) parents[i] = i;
    int weight = 0;
    int MSTcnt = 0;
    for(auto iter: edges){
        cout << get<1>(iter) << " - " << get<2>(iter) << "(" << get<0>(iter) << ")";
        if(!IsUnion(parents, get<1>(iter), get<2>(iter))){
            cout << " is condition valid. ";
            weight += get<0>(iter);
            Union(parents, get<1>(iter), get<2>(iter));
        }
        cout << "\n";
    }
    cout << weight;
}