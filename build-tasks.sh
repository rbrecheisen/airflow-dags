#!/bin/bash

for dag_dir in $(ls); do
  if [ -d ${dag_dir} ]; then
    echo "Building tasks for DAG ${dag_dir}..."
    cd ${dag_dir}
    for task_dir in $(ls); do
      if [ -d ${task_dir} ]; then
        echo "> ${task_dir}"
        cd ${task_dir}
        echo " > Building task ${task_dir}..."
        docker build -t brecheisen/${dag_dir}-${task_dir}:latest .
      fi
    done
  fi
done
