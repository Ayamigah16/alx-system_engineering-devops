#!/usr/bin/env ruby

# Search for "hbt" followed by one or more
# "n" characters and print the result.
puts ARGV[0].scan(/hbt{1,4}n/).join
