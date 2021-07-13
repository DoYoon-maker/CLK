#include <iostream>

using namespace std;

int main(int argc, char* argv)
{
	int n, k;

	cin >> n >> k;

	int *variety = new int[n];

	for (int count = 0; count < n; count++)
	{
		int inst;

		cin >> inst;

		variety[count] = inst;
	}

	int cur_index = n - 1, cur_coin = 0;

	while (cur_index >= 0)
	{
		if (variety[cur_index] <= k)
		{
			k = k - variety[cur_index];

			//cout << variety[cur_index] << "원을 차감하였습니다." << '\n';

			cur_coin++;

			//cout << "현재 남은 돈 : " << k << "현재 쌓인 코인" << cur_coin << '\n';
		}

		else cur_index--;
	}

	cout << cur_coin;
}