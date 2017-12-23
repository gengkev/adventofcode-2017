#include <iostream>

using namespace std;

const int PRIMES[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397};
const int NPRIMES = sizeof(PRIMES) / sizeof(PRIMES[0]);

int main(void) {
  long long a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;

  b = 99;
  c = b;
  if (a != 0) {
    b = b * 100 + 100000;
    c = b + 17000;
  }
  cerr << "b: " << b << ", c: " << c << endl;

  while (true) {
    /*
    bool is_prime = true;
    for (int i = 0; i < NPRIMES; i++) {
      if (b % PRIMES[i] == 0) {
        is_prime = false;
        break;
      }
    }
    if (!is_prime) {
      h++;
    }
    */

    f = 1;
    d = 2;

    do {
      /*
      e = 2;
      //cerr << "d: " << d << ", e: " << e << ", b: " << b
      //  << ", d*e-b: " << (d*e-b) << endl;
      do {
        //g = d * e - b;
        if (d * e == b) f = 0;
        e++;
        //g = e - b;
      } while (e != b);
      */

      if (b % d == 0) f = 0;

      d++;
      //g = d - b;
    } while (d != b);

    if (f == 0) {
      h++;
      cerr << "h is now " << h << endl;
    }

    //g = b - c;
    cerr << "end of loop, b = " << b << endl;
    if (b != c) {
      b += 17;
    } else {
      break;
    }
  }

  cerr << "h is " << h << endl;
  return 0;
}


