// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import Link from "next/link";

export function Logo() {
  return (
    <Link
      className="opacity-70 transition-opacity duration-300 hover:opacity-100"
      href="/"
    >
      <div className="flex items-center">
        <img
        src="/images/xiaotai_logo.png"
        alt="XiaoTai"
        className="ml-2 mr-2"
        style={{ width: '32px', height: '32px' }}
      />
      小太 AI深度研究助手
      </div>
    </Link>
  );
}
