#!/usr/bin/env ruby

# Check if the argument starts with "hb" followed
# by zero or one occurence of "t" character and print the result
puts ARGV[0].scan(/hb?tn/).join
