#include <iostream>
#include <string>

using namespace std;

string getToken(istream& is)
{
	string s;
	is >> s;
	return s;
}

void swap(int& a, int& b)
{
	int temp = a;

	a = b;
	
	b = temp;
}

void selection_sort(int* arr, int n)
{
	for (int count = 0; count < n; count++)
	{
		int minimum = arr[count], minimum_index = count;

		for (int count_ = count; count_ < n; count_++)
		{
			if (arr[count_] < minimum)
			{
				minimum = arr[count_];

				minimum_index = count_;
			}
		}

		swap(arr[count], arr[minimum_index]);
	}
}

int stairsum(int* arr, int n)
{
	int sum = 0;

	for (int count = 0; count < n; count++)
	{
		for (int count_ = 0; count_ <= count; count_++)
		{
			sum += arr[count_];
		}
	}

	return sum;
}

int main(int argc, char* argv)
{
	
	int num;

	cin >> num;
	
	istream& is = cin;

	string input_token;


	int* time = new int[num];
	
	for (int count = 0; count < num; count++)
	{
		input_token = getToken(is);

		time[count] = stoi(input_token);
	}

	selection_sort(time, num);

	cout << stairsum(time, num);
}