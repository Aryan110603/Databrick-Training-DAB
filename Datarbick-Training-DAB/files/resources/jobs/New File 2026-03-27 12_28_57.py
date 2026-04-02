resources:
  jobs:
    Training_Job:
      name: Training_Job
      tasks:
        - task_key: Staging
          notebook_task:
            notebook_path: /Workspace/Users/aaryansatere@gmail.com/Training/Notebook/Staging/Training
              sql
            source: WORKSPACE
        - task_key: Cleaned
          depends_on:
            - task_key: Staging
          notebook_task:
            notebook_path: /Workspace/Users/aaryansatere@gmail.com/Training/Notebook/Cleaned/Master_Cleaned
            source: WORKSPACE
          environment_key: Cleaned_environment
        - task_key: Datamart
          depends_on:
            - task_key: Cleaned
          notebook_task:
            notebook_path: /Workspace/Users/aaryansatere@gmail.com/Training/Notebook/Datamart/Master_Datamart
            source: WORKSPACE
      queue:
        enabled: true
      environments:
        - environment_key: Cleaned_environment
          spec:
            environment_version: "4"
      performance_target: PERFORMANCE_OPTIMIZED
