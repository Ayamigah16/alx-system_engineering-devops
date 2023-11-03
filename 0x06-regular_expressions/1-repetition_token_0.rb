#!/usr/bin/env ruby

# Check if the argument contains "hbt" followed by 2 to 5 characters and then "n" and print the result
puts ARGV[0].scan(/hbt{2,5}n/).join
