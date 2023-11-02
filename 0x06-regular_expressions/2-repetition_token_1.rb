#!/usr/bin/env ruby

# Check if the argument starts with "hb" followed
# by one or more "t" characters and print the result
puts ARGV[0].scan(/hb+t/).join
