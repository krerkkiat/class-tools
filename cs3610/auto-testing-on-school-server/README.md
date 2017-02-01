# auto-testing-on-school-server
I am too lazy to use scp or FileZilla so...

As Mr. Gray mentioned that the code should be test on the machine in Stocker lab. If you want to take that seriously, but don't want to repeatedly run scp to copy files to the machine in Stocker. (or using FileZilla to transfer files).

Another way could be setting up the Git "bare" repository on your account (on Stocker machine) as being described in [here](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server). You don't have to setup the SSH public keys since you can type in your account's password. Similarly, you can use your own account, so no need to create new one.

After that you can create hook named "post-receive" so that it compiles and runs your code on the Stocker's machine when you push new commit to the repository. More about the hooks is [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

These images show the running example of my implementation. Please keep in mind that I am not properly examine the code for the potential security issue that could occur, so use it at your own risk. I am not responsible for any damage that could happen.

Please also note that "...hosting [others'] code under your server could leave you open to charges of plagerism just because you have the ability to look at their code. I suggest you avoid that..." (J. E. Tysko, System Administrator, personal communication, January 17, 2017).
