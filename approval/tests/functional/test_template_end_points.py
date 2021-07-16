""" Module for testing Approval Templates """
import json
import pytest
from django.urls import reverse
from approval.tests.factories import TemplateFactory
from approval.tests.factories import WorkflowFactory
from approval.tests.factories import TenantFactory


@pytest.mark.django_db
def test_template_list(api_request):
    """Get a list of templates"""
    TemplateFactory()
    url = reverse("approval:template-list")
    response = api_request("get", url)

    assert response.status_code == 200
    content = json.loads(response.content)

    assert content["count"] == 1


@pytest.mark.django_db
def test_template_retrieve(api_request):
    """RETRIEVE a template by its id"""
    template = TemplateFactory()
    url = reverse("approval:template-detail", args=(template.id,))
    response = api_request("get", url)

    assert response.status_code == 200
    content = json.loads(response.content)
    assert content["id"] == template.id


@pytest.mark.django_db
def test_template_delete(api_request):
    """DELETE on a template should succeed"""
    template = TemplateFactory()
    url = reverse("approval:template-detail", args=(template.id,))
    response = api_request("delete", url)

    assert response.status_code == 204


@pytest.mark.django_db
def test_template_patch(api_request):
    """PATCH on a template should succeed"""
    template = TemplateFactory()
    url = reverse("approval:template-detail", args=(template.id,))
    response = api_request("patch", url, {"title": "update"})

    assert response.status_code == 200


@pytest.mark.django_db
def test_portfolio_put_not_supported(api_request):
    """PUT on a template should fail"""
    template = TemplateFactory()
    url = reverse("approval:template-detail", args=(template.id,))
    response = api_request("put", url, {"title": "update"})

    assert response.status_code == 405


@pytest.mark.django_db
def test_template_post(api_request):
    """Add a template"""
    TenantFactory()
    url = reverse("approval:template-list")
    response = api_request("post", url, {"title": "abcdef", "description": "abc"})

    assert response.status_code == 201


@pytest.mark.django_db
def test_template_workflows_get(api_request):
    """Fetch workflows for a template"""
    template = TemplateFactory()
    workflow = WorkflowFactory(template=template)
    url = reverse("approval:template-workflows", args=(template.id,))
    response = api_request("get", url)

    assert response.status_code == 200
    content = json.loads(response.content)

    assert content["count"] == 1
    assert content["results"][0]["id"] == workflow.id