#!/usr/bin/env ruby

# Check if the argument contains "hbtn" followed by one or more "n" characters and print the result
puts ARGV[0].scan(/hbt+n/).join
