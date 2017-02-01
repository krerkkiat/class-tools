# auto-testing-on-school-server
I am too lazy to use scp or FileZilla so...

As Mr. Gray mentioned that the code should be test on the machine in Stocker lab. If you want to take that seriously, but don't want to repeatedly run scp to copy files to the machine in Stocker. (or using FileZilla to transfer files).

Another way could be setting up the Git "bare" repository on your account (on Stocker machine) as being described in [here](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server). You don't have to setup the SSH public keys since you can type in your account's password. Similarly, you can use your own account, so no need to create new one.

After that you can create hook named "post-receive" so that it compiles and runs your code on the Stocker's machine when you push new commit to the repository. More about the hooks is [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

These images show the running example of my implementation. Please keep in mind that I am not properly examine the code for the potential security issue that could occur, so use it at your own risk. I am not responsible for any damage that could happen.

Please also note that "...hosting [others'] code under your server could leave you open to charges of plagerism just because you have the ability to look at their code. I suggest you avoid that..." (J. E. Tysko, System Administrator, personal communication, January 17, 2017).

# Steps
With that being said, here is the step by step of how to set the repository up.

0. Provide that your project is organized in the same way as the project 1 that Mr. Gray give to us (e.g. having folder called source/, the input files in the examples/)

On School Machine:

1. Make a directory for your project. e.g. project1.git
2. `cd` into the directory and run `git init --bare`
3. Copy a `post-receive` script into hooks/. Either by scp (pscp) or FileZilla.
4. Make note of the absolute path to this folder. (run `pwd` to show the current path)

On your local machine (e.g. laptop, PC at home, etc.)

1. Make a directory for your project (again, I know)
2. `cd` into it and run `git init`. Note that this time you don't need '--bare'.
3. Config the remote repository by pointing it to the folder in your account on school machine. The `git remote add origin <your username>@<school machine host name>:<absolute path to your project folder>` should take care of that.
- e.g. `git remote add origin kc@schoolserver.edu:/home/kc/subjects/cs3610/projects/project1.git` In this case, the <username> is "kc"; the <school machine host name> is "schoolserver.edu"; the <absolute path to your project folder> "is /home/kc/subjects/cs3610/projects/project1.git"
4. Set up the Makefile in the source folder. Make sure that it has build and run target.
5. Now you can try to commit and use git push to push to the school machine
6. The hook script will then automatically run the `make build` and `make run`. The result will be returned back to your local terminal by Git.
