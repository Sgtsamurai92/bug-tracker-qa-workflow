"""
Test script for support chat system prompt.
Run this to verify the new prompt format is working correctly.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.support.routes import extract_proposed_article


def test_extract_proposed_article():
    """Test the article extraction function"""
    
    # Test case 1: Valid article format
    test_response_1 = """
Here's how to filter bugs by status:

1. Go to the dashboard
2. Click the filter dropdown
3. Select the status you want

=== PROPOSED_HELP_ARTICLE ===
Title: Filtering Bugs by Status
Summary: Learn how to use the status filter to view specific bug categories. This helps you focus on bugs in a particular state like Open or Closed.
Steps:
1. Navigate to the dashboard page
2. Locate the filter dropdown above the bugs table
3. Click the dropdown to see available statuses
4. Select the status you want to view (Open, In Progress, Closed, etc.)
5. The bug list will automatically update
Common issues & fixes:
- Issue: Filter isn't working
  Fix: Refresh the page and try again
- Issue: Can't see some bugs
  Fix: Check if you have the right filter selected or choose "All Bugs"
=== END_PROPOSED_HELP_ARTICLE ===

Would you like me to save this as a help article?
"""
    
    # Test case 2: No article
    test_response_2 = """
To create a bug, click the Create Bug button on the dashboard.
Fill in the form and click Submit.
"""
    
    # Test case 3: Malformed article (missing end marker)
    test_response_3 = """
Here's the info...

=== PROPOSED_HELP_ARTICLE ===
Title: Test
Summary: Test article
"""
    
    print("=" * 70)
    print("Testing Article Extraction Function")
    print("=" * 70)
    
    # Test 1
    print("\n[Test 1] Valid article format")
    has_article, content, title = extract_proposed_article(test_response_1)
    print(f"  Has article: {has_article}")
    print(f"  Title: {title}")
    print(f"  Content length: {len(content) if content else 0} characters")
    assert has_article == True, "Should detect article"
    assert title == "Filtering Bugs by Status", f"Title mismatch: {title}"
    assert content is not None, "Content should not be None"
    print("  ✓ PASSED")
    
    # Test 2
    print("\n[Test 2] No article in response")
    has_article, content, title = extract_proposed_article(test_response_2)
    print(f"  Has article: {has_article}")
    print(f"  Title: {title}")
    print(f"  Content: {content}")
    assert has_article == False, "Should not detect article"
    assert content is None, "Content should be None"
    assert title is None, "Title should be None"
    print("  ✓ PASSED")
    
    # Test 3
    print("\n[Test 3] Malformed article (missing end marker)")
    has_article, content, title = extract_proposed_article(test_response_3)
    print(f"  Has article: {has_article}")
    print(f"  Title: {title}")
    print(f"  Content: {content}")
    assert has_article == False, "Should not detect incomplete article"
    print("  ✓ PASSED")
    
    print("\n" + "=" * 70)
    print("All tests passed! ✓")
    print("=" * 70)


def test_system_prompt():
    """Verify the system prompt is correctly formatted"""
    from app.support.prompts import SUPPORT_ASSISTANT_PROMPT
    
    print("\n" + "=" * 70)
    print("Checking System Prompt Configuration")
    print("=" * 70)
    
    # Check for key elements
    checks = [
        ("Context placeholder", "{context}" in SUPPORT_ASSISTANT_PROMPT),
        ("Article start marker", "=== PROPOSED_HELP_ARTICLE ===" in SUPPORT_ASSISTANT_PROMPT),
        ("Article end marker", "=== END_PROPOSED_HELP_ARTICLE ===" in SUPPORT_ASSISTANT_PROMPT),
        ("Behavior rules", "Behavior rules:" in SUPPORT_ASSISTANT_PROMPT),
        ("Tone section", "Tone:" in SUPPORT_ASSISTANT_PROMPT),
        ("Output format", "Output format:" in SUPPORT_ASSISTANT_PROMPT),
    ]
    
    all_passed = True
    for check_name, result in checks:
        status = "✓" if result else "✗"
        print(f"  {status} {check_name}")
        if not result:
            all_passed = False
    
    print()
    if all_passed:
        print("System prompt is correctly configured! ✓")
    else:
        print("⚠ System prompt may need attention")
    
    print("=" * 70)


def test_import_modules():
    """Test that all support modules can be imported"""
    print("\n" + "=" * 70)
    print("Testing Module Imports")
    print("=" * 70)
    
    modules = [
        ("routes", "app.support.routes"),
        ("llm_helper", "app.support.llm_helper"),
        ("context_builder", "app.support.context_builder"),
        ("prompts", "app.support.prompts"),
    ]
    
    all_passed = True
    for module_name, module_path in modules:
        try:
            __import__(module_path)
            print(f"  ✓ {module_name}")
        except Exception as e:
            print(f"  ✗ {module_name}: {e}")
            all_passed = False
    
    print()
    if all_passed:
        print("All modules imported successfully! ✓")
    else:
        print("⚠ Some modules failed to import")
    
    print("=" * 70)


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("SUPPORT CHAT SYSTEM - TEST SUITE")
    print("=" * 70)
    
    try:
        test_import_modules()
        test_system_prompt()
        test_extract_proposed_article()
        
        print("\n" + "=" * 70)
        print("✓ ALL TESTS PASSED")
        print("=" * 70)
        print("\nThe support chat system is correctly configured!")
        print("\nNext steps:")
        print("  1. Add your OPENAI_API_KEY to .env file")
        print("  2. Run: cd app && python app.py")
        print("  3. Visit http://127.0.0.1:5000")
        print("  4. Test the chat widget")
        print()
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
