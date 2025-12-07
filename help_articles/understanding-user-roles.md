# Understanding User Roles

_Generated on 2025-12-07_

The Bug Tracker has two user roles with different permissions and capabilities. Understanding these roles will help you know what you can and cannot do in the application.

## The Two Roles

### 1. Reporter Role

**Who is this for?**
- Team members who report bugs
- QA testers
- Developers who find issues
- Anyone who needs to document bugs

**What can Reporters do?**
✅ Create new bug reports
✅ View all bug reports in the system
✅ Edit their own bug reports
✅ Delete their own bug reports
✅ Filter and search bugs
✅ Assign bugs to team members
✅ Comment on bugs (if enabled)

**What can't Reporters do?**
❌ Edit other people's bug reports
❌ Delete other people's bug reports
❌ Generate system-wide reports
❌ Manage user accounts

**Default Test Account:**
- Email: `reporter@example.com`
- Password: `password123`

---

### 2. Manager Role

**Who is this for?**
- Project managers
- Team leads
- Administrators
- Senior developers

**What can Managers do?**
✅ Everything a Reporter can do, PLUS:
✅ Edit **any** bug report (not just their own)
✅ Delete **any** bug report
✅ Change bug assignments
✅ Update bug statuses
✅ Generate HTML reports
✅ View bug statistics
✅ Manage workflows

**Default Test Account:**
- Email: `manager@example.com`
- Password: `password123`

---

## Permission Comparison Table

| Action | Reporter | Manager |
|--------|----------|---------|
| Create bugs | ✅ Yes | ✅ Yes |
| View all bugs | ✅ Yes | ✅ Yes |
| Edit own bugs | ✅ Yes | ✅ Yes |
| Edit others' bugs | ❌ No | ✅ Yes |
| Delete own bugs | ✅ Yes | ✅ Yes |
| Delete others' bugs | ❌ No | ✅ Yes |
| Assign bugs | ✅ Yes | ✅ Yes |
| Filter/search | ✅ Yes | ✅ Yes |
| Generate reports | ❌ No | ✅ Yes |

## How to Tell Your Role

When you're logged in, look at the top-right corner of the navigation bar:
- Your email is displayed
- Next to it is a badge showing your role
- It will say either **reporter** or **manager**

## Role-Based Restrictions

### When Editing Bugs
- **Reporters**: Only see "Edit" button on bugs they created
- **Managers**: See "Edit" button on all bugs

### When Deleting Bugs
- **Reporters**: Only see "Delete" button on bugs they created
- **Managers**: See "Delete" button on all bugs

### Error Messages
If you try to perform an action you don't have permission for:
- "Permission denied" message appears
- Contact your manager if you need different permissions

## Common Questions

**Q: Can my role be changed?**
A: Yes, a system administrator can upgrade you from Reporter to Manager or vice versa.

**Q: Can I have different roles in different projects?**
A: Currently, roles are system-wide, not project-specific.

**Q: What happens if I delete a bug as a Reporter?**
A: You can only delete bugs you created. The bug is permanently removed from the system.

**Q: Can Reporters see other people's bugs?**
A: Yes! All bugs are visible to all users. The restriction is only on editing and deleting.

**Q: Do Managers get notified when bugs are created?**
A: This depends on your notification settings (if configured).

## Best Practices by Role

### For Reporters:
1. Document bugs thoroughly when creating them
2. Keep your bug reports updated
3. Don't delete bugs unless absolutely necessary
4. Communicate with assignees about status

### For Managers:
1. Review new bugs regularly
2. Assign bugs to appropriate team members
3. Update statuses to reflect progress
4. Use reports to track team performance
5. Only delete bugs after careful consideration

## Need Help?

- Check the [Getting Started Guide](../docs/getting-started.md)
- Learn [How to Create a Bug Report](./how-to-create-a-bug-report.md)
- Ask the support chat for assistance
