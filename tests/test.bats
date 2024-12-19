#!/usr/bin/env bats

@test "mage2gen service should start" {
  run ddev start
  [ "$status" -eq 0 ]
  sleep 10  # Give the service time to start
  run ddev exec curl http://localhost:8000
  [ "$status" -eq 0 ]
}