#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <unistd.h>
using namespace std;

int main() {
    cout << "Starting main" << endl;
    int file_fd = open("text.txt", O_WRONLY | O_TRUNC | O_CREAT, 0666);
    dup2(file_fd, STDOUT_FILENO);
    pid_t child_pid = fork();
    if (child_pid != 0) {
        wait(NULL);
        cout << "ECS 150, in parent" << endl;
    }
    else {
        cout << "ECS 150, in child" << endl;
    }
    cout << "Ending main: " << child_pid << endl;
}