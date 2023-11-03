#!/usr/bin/env ruby

# Check if the argument contains "hbt" followed by 0 to 5 characters and then "n" and print the result
puts ARGV[0].scan(/hbt.{0,5}n/).join
