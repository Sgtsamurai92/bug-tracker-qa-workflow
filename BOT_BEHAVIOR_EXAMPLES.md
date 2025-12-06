# Support Bot Behavior Examples

This document shows how the updated support bot will respond to various types of questions.

## In-Scope Questions (Bug Tracker Features)

### Example 1: Basic Feature Question

**User:** "How do I create a bug report?"

**Bot Response:**
```
To create a bug report:

1. Click the "Create Bug" button on the dashboard
2. Fill in the required fields:
   • Title - A brief summary of the bug
   • Description - Detailed information about the issue
   • Severity - Choose Critical, High, Medium, or Low
   • Priority - How urgent the fix is
   • Status - Usually starts as "Open"
3. Optionally assign the bug to a team member
4. Click "Submit" to save the bug report

The new bug will appear in your dashboard table.

See: 'Getting Started Guide' for more details about creating bugs.
```

### Example 2: Role & Permissions Question

**User:** "What's the difference between a reporter and a manager?"

**Bot Response:**
```
The Bug Tracker has two user roles with different permissions:

**Reporter:**
• Can create new bug reports
• Can view all bugs
• Can edit their own bug reports only
• Cannot delete any bugs

**Manager:**
• All Reporter capabilities, plus:
• Can edit ANY bug report (not just their own)
• Can delete bug reports
• Can change bug status and assignments
• Can generate reports

Default test accounts:
• Reporter: reporter@example.com / password123
• Manager: manager@example.com / password123

See: 'Understanding User Roles' for more details.
```

### Example 3: Workflow Question

**User:** "How do I filter bugs by status?"

**Bot Response:**
```
To filter bugs by status:

1. Go to the dashboard page
2. Look for the filter dropdown above the bugs table
3. Click the dropdown to see available statuses:
   • All Bugs (default)
   • Open
   • In Progress
   • Closed
   • Fixed
   • Reopened
   • Won't Fix
4. Select the status you want to view
5. The bug list automatically updates to show only bugs with that status

This helps you focus on specific categories of bugs, like viewing only open issues that need attention.
```

---

## Out-of-Scope Questions (Features NOT in Bug Tracker)

### Example 1: Project Management

**User:** "How do I create a project or organize bugs into projects?"

**Bot Response:**
```
That's not a feature this Bug Tracker application currently provides. This app is focused on tracking and managing bug reports.

Here are some helpful resources to get you started with what the app does offer:
• Getting Started Guide - Learn the basics of the Bug Tracker
• How to Create a Bug Report - Step-by-step guide for reporting bugs
• Understanding User Roles - Learn about Reporter and Manager permissions

Is there anything about bug tracking or managing bug reports I can help you with?
```

### Example 2: API Access

**User:** "How can I access the API to integrate with my CI/CD pipeline?"

**Bot Response:**
```
That's not a feature this Bug Tracker application currently provides. This app is focused on tracking and managing bug reports.

Here are some helpful resources to get you started with what the app does offer:
• Getting Started Guide - Learn the basics of the Bug Tracker
• How to Create a Bug Report - Step-by-step guide for reporting bugs
• Understanding User Roles - Learn about Reporter and Manager permissions

Is there anything about bug tracking or managing bug reports I can help you with?
```

### Example 3: Time Tracking

**User:** "How do I log hours spent fixing a bug?"

**Bot Response:**
```
That's not a feature this Bug Tracker application currently provides. This app is focused on tracking and managing bug reports.

Here are some helpful resources to get you started with what the app does offer:
• Getting Started Guide - Learn the basics of the Bug Tracker
• How to Create a Bug Report - Step-by-step guide for reporting bugs
• Understanding User Roles - Learn about Reporter and Manager permissions

Is there anything about bug tracking or managing bug reports I can help you with?
```

### Example 4: Mobile App

**User:** "Is there a mobile app I can download?"

**Bot Response:**
```
That's not a feature this Bug Tracker application currently provides. This app is focused on tracking and managing bug reports.

Here are some helpful resources to get you started with what the app does offer:
• Getting Started Guide - Learn the basics of the Bug Tracker
• How to Create a Bug Report - Step-by-step guide for reporting bugs
• Understanding User Roles - Learn about Reporter and Manager permissions

Is there anything about bug tracking or managing bug reports I can help you with?
```

### Example 5: Third-Party Integrations

**User:** "Can I connect this to Jira or GitHub?"

**Bot Response:**
```
That's not a feature this Bug Tracker application currently provides. This app is focused on tracking and managing bug reports.

Here are some helpful resources to get you started with what the app does offer:
• Getting Started Guide - Learn the basics of the Bug Tracker
• How to Create a Bug Report - Step-by-step guide for reporting bugs
• Understanding User Roles - Learn about Reporter and Manager permissions

Is there anything about bug tracking or managing bug reports I can help you with?
```

---

## Questions About Missing Features (Within Scope)

### Example 1: Feature Not Yet Implemented

**User:** "How do I bulk edit multiple bugs at once?"

**Bot Response:**
```
Currently, the Bug Tracker doesn't have a bulk edit feature. You'll need to edit bugs one at a time:

1. Navigate to the dashboard
2. Click "Edit" on the first bug you want to change
3. Make your changes and click "Update Bug"
4. Return to the dashboard and repeat for the next bug

**Tip:** Use the status filter to narrow down the bugs you're working with, which can help you stay organized.

=== PROPOSED_HELP_ARTICLE ===
Title: Editing Multiple Bug Reports
Summary: While bulk editing isn't available, this article shows you efficient strategies for updating multiple bug reports when you need to make similar changes across several items.
Steps:
1. Use the status filter to show only the bugs you need to edit
2. Edit bugs one at a time using the Edit button
3. Keep a checklist or notes to track which bugs you've updated
4. Consider using browser tabs to open multiple bugs for comparison
Common issues & fixes:
- Issue: Losing track of which bugs I've already edited
  Fix: Use the filter to focus on a specific status, and change status after editing
- Issue: Changes aren't saving
  Fix: Always click "Update Bug" before navigating away from the edit page
=== END_PROPOSED_HELP_ARTICLE ===

Would you like me to save this as a help article for future reference?
```

### Example 2: Clarification Needed

**User:** "The bug list isn't working right."

**Bot Response:**
```
I'd like to help! Can you tell me a bit more about what's happening?

For example:
• Are bugs not showing up in the list?
• Is the filter not working correctly?
• Are you seeing an error message?
• Are you unable to edit or delete bugs?

The more details you can share, the better I can assist you with the Bug Tracker.
```

---

## Summary of Bot Behavior

### ✅ Will Answer Questions About:
- Creating bug reports
- Editing and deleting bugs
- Filtering bugs by status
- User roles (Reporter vs Manager)
- Login and authentication
- Bug statuses (Open, In Progress, Closed, etc.)
- Bug severity and priority levels
- Dashboard features
- Report generation
- Permissions and access control

### ❌ Will Redirect Questions About:
- Project management features
- Time tracking
- Code repositories
- CI/CD integrations
- API access
- Mobile applications
- Third-party tool integrations
- Email notifications
- Custom workflows outside bug tracking
- Any feature not in the core bug tracker

### 📝 Will Propose Help Articles For:
- Common questions about actual Bug Tracker features
- Workflows and best practices for bug tracking
- Troubleshooting common issues
- Efficient use of existing features

### 🔗 Standard Redirect Links:
When redirecting out-of-scope questions, the bot always suggests:
1. **Getting Started Guide** - Basics of the Bug Tracker
2. **How to Create a Bug Report** - Step-by-step guide
3. **Understanding User Roles** - Reporter and Manager permissions

---

## Testing the Bot

To test the updated behavior:

1. **Test in-scope questions:**
   - "How do I create a bug?"
   - "What's the difference between reporter and manager?"
   - "How do I delete a bug?"

2. **Test out-of-scope questions:**
   - "Can I integrate with Slack?"
   - "Is there an API?"
   - "How do I track time on bugs?"

3. **Test edge cases:**
   - "How do I bulk edit bugs?" (should propose article)
   - "It's not working" (should ask for clarification)
   - "What features does this app have?" (should summarize core features)

4. **Verify redirect format:**
   - Check that out-of-scope responses include the exact 3 bullet points
   - Verify friendly tone is maintained
   - Ensure it asks follow-up question about bug tracking

---

**Last Updated:** December 6, 2025  
**Prompt Version:** 2.1 (Bug Tracker Focused)
