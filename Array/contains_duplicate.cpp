#include <bits/stdc++.h>
#define fast_io                     \
  ios_base::sync_with_stdio(false); \
  cin.tie(NULL);                    \
  cout.tie(NULL);
using namespace std;

bool containsDuplicate(vector<int> &nums)
{
  set<int> st;
  for (int i = 0; i < nums.size(); i++)
  {
    if (st.find(nums[i]) == st.end())
    {
      st.insert(nums[i]);
    }
    else
    {
      return true;
    }
  }
  for(int x:st){
    cout<<x<<endl;
  }
  return false;
}
int main()
{
  fast_io;
  vector<int> v={5,1,6,3,4,};
  cout<<containsDuplicate(v);

  return 0;
}