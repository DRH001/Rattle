todo: format this

Here are some very basic examples of Rattle code

Format:
code         ->           output                             # comment

[p+]10       ->           0 1 2 3 4 5 6 7 8 9                # count up, zero-indexed (in this example, loop 10 times)

[+p]10       ->           1 2 3 4 5 6 7 8 9 10               # count up, one-indexed

[+#p]10      ->           0 1 3 6 10 15 21 28 36 45          # 1+2+3+4+5+....+n

=1s[p+~$]10  ->           1 1 2 3 5 8 13 21 34 55            # generate fibonacci sequence


