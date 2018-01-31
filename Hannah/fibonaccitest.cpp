#include <iostream>
using namespace std;

int main() {
	int x = 1;
	int y = 2;
	int z = 0;
	int sum = 0;
	while (x < 4000000) {
		z = x + y;
		x = y;
		y = z;
		if ((z % 2) == 0) {
			sum = sum + z;
		}
	}
	cout << sum << endl;
	return sum;
}