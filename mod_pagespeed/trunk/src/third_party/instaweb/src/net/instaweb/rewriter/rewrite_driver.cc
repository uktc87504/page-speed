// Copyright 2010 and onwards Google Inc.
// Author: jmarantz@google.com (Joshua Marantz)

#include "net/instaweb/rewriter/public/rewrite_driver.h"

#include <assert.h>
#include "net/instaweb/htmlparse/public/html_parse.h"
#include "net/instaweb/rewriter/public/add_head_filter.h"
#include "net/instaweb/rewriter/public/base_tag_filter.h"
#include "net/instaweb/rewriter/public/css_sprite_filter.h"
#include "net/instaweb/rewriter/public/outline_filter.h"
#include "net/instaweb/rewriter/public/file_resource_manager.h"

namespace net_instaweb {

RewriteDriver::RewriteDriver(HtmlParse* html_parse, FileSystem* file_system)
    : html_parse_(html_parse),
      add_head_filter_(NULL),
      base_tag_filter_(NULL),
      file_resource_manager_(NULL),
      css_sprite_filter_(NULL),
      outline_filter_(NULL),
      file_system_(file_system) {
}

RewriteDriver::~RewriteDriver() {
  if (add_head_filter_ != NULL) {
    delete add_head_filter_;
  }
  if (base_tag_filter_ != NULL) {
    delete base_tag_filter_;
  }
  if (file_resource_manager_ != NULL) {
    delete file_resource_manager_;
  }
  if (css_sprite_filter_ != NULL) {
    delete css_sprite_filter_;
  }
  if (outline_filter_ != NULL) {
    delete outline_filter_;
  }
}

void RewriteDriver::AddHead() {
  if (add_head_filter_ == NULL) {
    add_head_filter_ = new AddHeadFilter(html_parse_);
    html_parse_->AddFilter(add_head_filter_);
  }
}

void RewriteDriver::SetBase(const char* base) {
  AddHead();
  if (base_tag_filter_ == NULL) {
    base_tag_filter_ = new BaseTagFilter(html_parse_);
    html_parse_->AddFilter(base_tag_filter_);
  }
  base_tag_filter_->set_base(base);
}

void RewriteDriver::SetResources(
    const char* file_prefix, const char* serving_prefix, int num_shards) {
  if (file_resource_manager_ != NULL) {
    delete file_resource_manager_;
  }
  file_resource_manager_ = new FileResourceManager(
      file_prefix, serving_prefix, num_shards, file_system_);
}

void RewriteDriver::SpriteCssFiles() {
  assert(file_resource_manager_);
  assert(css_sprite_filter_ == NULL);
  css_sprite_filter_ = new CssSpriteFilter(html_parse_, file_resource_manager_);
  html_parse_->AddFilter(css_sprite_filter_);
}

void RewriteDriver::OutlineResources() {
  // TODO(sligocki): Use FatalError rather than assert.
  assert(file_resource_manager_);
  assert(outline_filter_ == NULL);
  outline_filter_ = new OutlineFilter(html_parse_, file_resource_manager_);
  html_parse_->AddFilter(outline_filter_);
}
}