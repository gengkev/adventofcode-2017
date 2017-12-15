#include <iostream>

using namespace std;

const long long MOD = 2147483647;
//const long long ITERS = 40000000;  // star 1
const long long ITERS = 5000000;  // star 2

int main() {
//  long long a = 65, b = 8921;
  long long a = 699, b = 124;

  // star 2
  while (a % 4 != 0)
    a = (a * 16807) % MOD;
  while (b % 8 != 0)
    b = (b * 48271) % MOD;

  long long count = 0;
  for (long long i = 0; i < ITERS; i++) {
    long long a1 = a & 0xffff;
    long long b1 = b & 0xffff;
    if (a1 == b1) count++;

    a = (a * 16807) % MOD;
    b = (b * 48271) % MOD;

    // star 2
    while (a % 4 != 0)
      a = (a * 16807) % MOD;
    while (b % 8 != 0)
      b = (b * 48271) % MOD;
  }
  cout << count << endl;
  return 0;
}
