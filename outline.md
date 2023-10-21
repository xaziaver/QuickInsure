## QuickInsure: A Simple Property Insurance Quotation System

### Features:

1. **User Authentication**: Use Django's authentication.
2. **Quotation System**: Users input property details; the system provides a quote.
3. **Claim Submission**: Form-based input with image upload.
4. **Background Processing with Celery**: Email/notification for claim submission.
5. **Dynamic Pricing using Redis**: Use Redis for dynamic factors affecting insurance rates.
6. **Message System with Kafka**: Send messages on claim submission for analytics/auditing.

### Tech Stack:

- Backend: Django, Postgres
- Asynchronous Tasks: Celery, Redis
- Messaging: Kafka
- Deployment: Heroku

### Development Timeline:

1. **Week 1-2**: 
   - Django setup, database design.
   - User authentication.
   - Start basic quotation system (models, views).
2. **Week 3**:
   - Advance the quotation system (algorithm, user flow).
   - Begin claim submission feature.
3. **Week 4**: 
   - Complete claim submission.
   - Set up Celery for background processing.
4. **Week 5**:
   - Integrate Redis for dynamic pricing.
   - Setup Kafka for messaging.
5. **Week 6**:
   - Test, identify bugs, and improve features.
6. **Week 7**: 
   - Deploy on Heroku, set up CI/CD.
7. **Week 8**:
   - End-to-end testing, documentation, final tweaks.