import os
import google.generativeai as genai

genai.configure(api_key=os.environ["AIzaSyBWO8TBgYjv66jokW26QWJsXip7EszJr3Y"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "tips about mental health care",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Taking care of your mental health is crucial for overall well-being.  Here are some tips, categorized for clarity:\n\n**I.  Self-Care Strategies (Things you can do daily or regularly):**\n\n* **Prioritize Sleep:** Aim for 7-9 hours of quality sleep per night.  Establish a regular sleep schedule and create a relaxing bedtime routine.\n* **Healthy Diet:**  Nourish your body with nutritious foods.  Limit processed foods, sugar, and caffeine.  Stay hydrated.\n* **Regular Exercise:** Physical activity releases endorphins, which have mood-boosting effects. Find an activity you enjoy, whether it's walking, dancing, swimming, or team sports.  Even short bursts of activity are beneficial.\n* **Mindfulness and Meditation:** Practice mindfulness techniques like deep breathing or meditation to reduce stress and increase self-awareness.  Many apps are available to guide you.\n* **Connect with Others:** Spend time with loved ones, build strong relationships, and nurture your social connections.  Talking to someone you trust can make a significant difference.\n* **Engage in Hobbies:**  Dedicate time to activities you enjoy and find fulfilling.  This could be anything from reading to painting to gardening.\n* **Limit Screen Time:** Excessive screen time can negatively impact mental health.  Set boundaries and take breaks from devices.\n* **Spend Time in Nature:**  Being outdoors has been shown to reduce stress and improve mood.  Take walks in the park, hike in the woods, or simply sit and enjoy the sunshine.\n* **Journaling:** Writing down your thoughts and feelings can help you process emotions and gain perspective.\n* **Learn to Say No:** Setting healthy boundaries is crucial for protecting your mental well-being.  Don't overcommit yourself.\n\n\n**II. Seeking Professional Help:**\n\n* **Know When to Seek Help:**  If you're struggling with persistent sadness, anxiety, hopelessness, or other mental health challenges, don't hesitate to seek professional help.  It's a sign of strength, not weakness.\n* **Finding a Therapist:**  Research therapists in your area who specialize in the specific issues you're facing.  Consider factors like their experience, approach, and personality fit.\n* **Different Types of Therapy:**  Explore different types of therapy, such as Cognitive Behavioral Therapy (CBT), Dialectical Behavior Therapy (DBT), or others, to find what works best for you.\n* **Psychiatrists vs. Therapists:**  Psychiatrists are medical doctors who can prescribe medication, while therapists provide talk therapy.  You may benefit from both.\n* **Utilizing Support Groups:**  Connecting with others who share similar experiences can provide valuable support and understanding.\n\n\n**III.  Important Considerations:**\n\n* **Be Patient:**  Improving mental health takes time and effort.  Don't get discouraged if you don't see results immediately.\n* **Self-Compassion:**  Be kind to yourself and practice self-compassion.  Treat yourself with the same understanding and kindness you would offer a friend.\n* **Seek Emergency Help:**  If you're experiencing a mental health crisis, seek immediate help. Contact a crisis hotline, emergency services, or go to the nearest emergency room.\n\n\nThis is not an exhaustive list, and individual needs vary.  It's important to find what works best for you.  If you are concerned about your mental health, please reach out to a healthcare professional for personalized guidance and support.  Remember that you are not alone.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)