# Why _rhcpdl_ #
Well... the why behind the name is simple.
**R** ed **H** at **C** ustomer **P** ortal **D** own **L** oader

For the why behind its existence, read the Background section.

---

# Background #
For years many of us have been subscribers to Red Hat's Linux platform, or their other software.  In a world where we do not always have the joys of a Linux desktop, many of us would download software from their web site by copying the provided URL for the software, which is a short-term randomly generated URL, and then from the CLI of a server using wget or a similar utility to download the software.  A primary use case for this would be downloading the RHEL6 DVD to your local build server.

The recent roll-out of Red Hat Customer Portal (RHCP) made some significant changes to the overall user experience.  Many of these changes are very positive, such as single sign-on.  Unfortunately, one side effect was that the above use case has become very cumbersome.  The new randomly generated format introduces two complications when attempting to use at the CLI:

  1. The new URL format includes important information after an & character, which is lost on the Linux cli when not escaped due to the standard behavior the & character invokes of backgrounding the preceding process.  The remainder of the line is then lost.
  1. The resulting filename of a file downloaded using the new URL format includes all of the URL parameters, thus requiring the user to rename a file immediately after downloading it.

I opened a ticket in October of 2010 to address this concern, and in May of 2011 was told that the RFE to return this functionality was denied.  They did state that at some indeterminate time in the future they may re-write their downloading and fix this, but no promises.


---

# Long Term Goal #
To have Red Hat make this application obsolete by restoring the functionality it provides to their clients.


---

# Features #
  * Performs a download of any URL provided (not just RHCP, but RHCP is the only real reason to use this over wget or curl, and I make no promises about the output on any other URL such as from sourceforge). Specifically targeted at the following downloadable file types:
    * .iso
    * .exe
    * .vfd
    * .rpm
  * Ensures that the downloaded filename does not include any HTML parameters
  * Let you know that the URL has expired if you took to long to use the generated one from RHCP
  * Provides you with an MD5 checksum of the downloaded file


---

# What this is not #
  * Does not allow you to download files you do not have access to
  * Does not do anything you can't already do in several standard CLI commands


---

# Usage #
```
# rhcpdl "<url>"
```
or
```
# rhcpdl <url>
```

Both methods work.  The first method keeps the entire process in the foreground, while the second method corrects your URL to re-add the missing component while letting the process run in the background.  I realize that the quoting was one of the complaints above, and that is why both methods are supported.  I'd rather be flexible.  To be honest the unquoted fits my work flow better because I usually background the process on my own.



---

# Todo #

  * Build RHEL4/5/6 rpms - method is in place, just need the build servers
  * Use threading to background the download so that I can display a status bar like wget
  * Support SHA-256 checksums
  * Make checksum generations optional, triggered by cli switch?
  * Possibly support multiple URLs if each is quoted?