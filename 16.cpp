#include <fstream>
#include <iostream>
#include <cctype>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <vector>

using namespace std;


struct Command {
  char c;
  union {
    struct {
      int x;
    } spin;
    struct {
      int a;
      int b;
    } exchange;
    struct {
      char a;
      char b;
    } partner;
  } data;
};

/*
const int N = 5;
const int num_dances = 2;
const char *filename = "sample.txt";
*/

const int N = 16;
const int num_dances = 1000000000;
const char *filename = "input.txt";

void reverse_arr(char *A, int start, int end) {
  int len = end - start;
  for (int i = 0; i < len / 2; i++) {
    swap(A[start + i], A[end - i - 1]);
  }
}

int main() {
  vector<Command> commands;
  string line;
  ifstream infile(filename);
  while (getline(infile, line, ',')) {
    struct Command cmd;
    cmd.c = line[0];
    if (line[0] == 's') {
      cmd.data.spin.x = atoi(line.c_str() + 1);
    } else {
      int index = 1;
      while (line[index] != '/') index++;
      line[index] = '\0';

      if (line[0] == 'x') {
        assert(index == 2 || index == 3);
        cmd.data.exchange.a = atoi(line.c_str() + 1);
        cmd.data.exchange.b = atoi(line.c_str() + index + 1);
      } else {
        assert(index == 2);
        cmd.data.partner.a = line[1];
        cmd.data.partner.b = line[index + 1];
      }
    }
    commands.push_back(cmd);
  }
  infile.close();

  char A[N+1];
  for (int i = 0; i < N; i++) {
    A[i] = (char) ('a' + i);
  }
  A[N] = '\0';

  for (int d = 0; d < num_dances; d++) {
    if (d % 10000 == 0) {
      fprintf(stderr, "iteration d = %d\n", d);
    }
    for (Command cmd : commands) {
      //fprintf(stderr, "init: %s\n", A);
      if (cmd.c == 's') {
        // reverse 0 to N-n, N-n to N
        int n = cmd.data.spin.x;
        reverse_arr(A, 0, N-n);
        reverse_arr(A, N-n, N);
        reverse_arr(A, 0, N);
      }
      else if (cmd.c == 'x') {
        int a = cmd.data.exchange.a;
        int b = cmd.data.exchange.b;
        swap(A[a], A[b]);
      }
      else if (cmd.c == 'p') {
        char a = cmd.data.partner.a;
        char b = cmd.data.partner.b;
        int apos = -1, bpos = -1;
        for (int i = 0; i < N; i++) {
          if (A[i] == a) apos = i;
          if (A[i] == b) bpos = i;
        }
        assert(apos != -1 && bpos != -1);
        swap(A[apos], A[bpos]);
      }
      else {
        assert(false);
      }
    }
  }

  printf("output: %s\n", A);

  return 0;
}


