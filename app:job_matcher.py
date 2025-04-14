
import openai

def match_jobs(resume_text, jobs):
    job_descriptions = "\n".join([f"{j['title']} at {j['company']} in {j['location']}" for j in jobs])
    prompt = f"""
    Match the resume with these job roles and rank them:

    Resume:
    {resume_text}

    Jobs:
    {job_descriptions}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content
