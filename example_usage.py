from client import MultiStepWebFormFillOrchestratorClient

def main():
    client = MultiStepWebFormFillOrchestratorClient()
    res = client.orchestrate_form_pipeline('USER_SIGNUP')
    print('Multi-Step Form Orchestrator: ' + res['orchestration_id'] + ' (' + res['submission_status'] + ')')
    print('Steps: ' + str(res['steps_completed']) + '/' + str(res['total_steps']) + ' | Errors: ' + str(res['validation_errors_detected']))
    print('Audit URL: ' + res['execution_audit_url'])

if __name__ == '__main__':
    main()
